[![pipeline status](https://gitlab.com/meltano/meltano/badges/master/pipeline.svg)](https://gitlab.com/meltano/meltano/commits/master)

# Meltano

Meltano is an open source convention-over-configuration product for the whole data lifecycle, all the way from loading data to analyzing it.

It does [data ops](https://en.wikipedia.org/wiki/DataOps), data engineering, analytics, business intelligence, and data science. It leverages open source software and software development best practices including version control, CI, CD, and review apps.

Meltano stands for the [steps of the data science life-cycle](#data-science-lifecycle): Model, Extract, Load, Transform, Analyze, Notebook, and Orchestrate.

## How to Install and Run Meltano  

Check out our [guide](https://meltano.com/guide/#getting-started) to getting started with Meltano.

## How to Install and Run Meltano.com

Currently our documentation is being generated by [VuePress](https://vuepress.vuejs.org) and it lives in the `/docs` directory. To run it locally, please run the following commands:

### Requirements

- [NodeJS 8+](https://nodejs.org/)

### Instructions

1. Install all dependencies
```bash
npm install
```

2. Run a local instance of VuePress that dynamically uploads as you make changes to the files in the `/docs` directory
```bash
npm run dev:docs
```

## Contributing to Meltano

We welcome contributions and improvements, please see the [contribution guidelines](https://meltano.com/docs/contributing.html)

## License

This code is distributed under the MIT license, see the [LICENSE](LICENSE) file.

[docker-compose]: https://docs.docker.com/compose/
