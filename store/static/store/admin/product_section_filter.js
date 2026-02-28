(function () {
  function updateSections() {
    var categoryField = document.getElementById('id_category');
    var sectionField = document.getElementById('id_section');
    if (!categoryField || !sectionField) return;

    var categoryId = categoryField.value;
    var currentValue = sectionField.value;
    var endpoint = '/admin/store/product/sections-by-category/';

    sectionField.innerHTML = '';
    var emptyOption = document.createElement('option');
    emptyOption.value = '';
    emptyOption.textContent = '---------';
    sectionField.appendChild(emptyOption);

    if (!categoryId) {
      sectionField.value = '';
      return;
    }

    fetch(endpoint + '?category_id=' + encodeURIComponent(categoryId), { credentials: 'same-origin' })
      .then(function (response) { return response.json(); })
      .then(function (data) {
        (data.results || []).forEach(function (item) {
          var option = document.createElement('option');
          option.value = item.id;
          option.textContent = item.name;
          if (String(item.id) === String(currentValue)) {
            option.selected = true;
          }
          sectionField.appendChild(option);
        });
      });
  }

  document.addEventListener('DOMContentLoaded', function () {
    var categoryField = document.getElementById('id_category');
    if (!categoryField) return;
    categoryField.addEventListener('change', updateSections);
    updateSections();
  });
})();
