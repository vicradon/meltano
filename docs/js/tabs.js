const removeActiveClasses = function (ulElement) {
  const lis = ulElement.querySelectorAll('li');
  Array.prototype.forEach.call(lis, function (li) {
    li.classList.remove('active');
  });
};

const getChildPosition = function (element) {
  let parent = element.parentNode;
  for (let i = 0; i < parent.children.length; i++) {
    if (parent.children[i] === element) {
      return i;
    }
  }

  throw new Error('No parent found');
};

window.addEventListener('load', function () {
  const tabLinks = document.querySelectorAll('ul.tab li a');

  Array.prototype.forEach.call(tabLinks, function (link) {
    link.addEventListener(
      'click',
      function (event) {
        event.preventDefault();

        let liTab = link.parentNode;
        let ulTab = liTab.parentNode;
        let position = getChildPosition(liTab);
        if (liTab.className.includes('active')) {
          return;
        }

        removeActiveClasses(ulTab);
        let tabContentId = ulTab.getAttribute('data-tab');
        let tabContentElement = document.getElementById(tabContentId);
        removeActiveClasses(tabContentElement);

        tabContentElement
          .querySelectorAll('li')
          [position].classList.add('active');
        liTab.classList.add('active');
      },
      false
    );
  });
});
