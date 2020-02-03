import logging
import click
import sys

from meltano.core.permissions import grant_permissions, SpecLoadingError
from meltano.core.tracking import GoogleAnalyticsTracker
from . import cli
from .params import project


@cli.group()
def permissions():
    """Database permission related commands."""
    pass


@permissions.command()
@click.argument("spec")
@click.option(
    "--db",
    help="The type of the target DB the specifications file is for.",
    type=click.Choice(["postgres", "snowflake"]),
    required=True,
)
@click.option("--dry", help="Do not actually run, just check.", is_flag=True)
@click.option(
    "--diff", help="Show full diff, both new and existing permissions.", is_flag=True
)
@project()
def grant(project, db, spec, dry, diff):
    """Grant the permissions provided in the provided specification file."""
    try:
        sql_commands = grant_permissions(db, spec, dry_run=dry)
        tracker = GoogleAnalyticsTracker(project)
        tracker.track_meltano_permissions_grant(db=db, dry=dry)

        click.secho()
        if diff:
            click.secho(
                "SQL Commands generated for given spec file (Full diff with both new and already granted commands):"
            )
        else:
            click.secho("SQL Commands generated for given spec file:")
        click.secho()

        diff_prefix = ""
        for command in sql_commands:
            if command["already_granted"]:
                if diff:
                    diff_prefix = "  "
                else:
                    continue
            else:
                if diff:
                    diff_prefix = "+ "

            if command.get("run_status"):
                fg = "green"
                run_prefix = "[SUCCESS] "
            elif command.get("run_status") is None:
                fg = "cyan"
                run_prefix = "[SKIPPED] "
            else:
                fg = "red"
                run_prefix = "[ERROR] "

            click.secho(f"{diff_prefix}{run_prefix}{command['sql']};", fg=fg)
    except SpecLoadingError as exc:
        for line in str(exc).splitlines():
            click.secho(line, fg="red")
        sys.exit(1)
