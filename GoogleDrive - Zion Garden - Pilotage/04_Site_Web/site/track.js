(function () {
  function pushEvent(name, params) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: name }, params || {}));
  }

  function bindClick(selector, eventName, extra) {
    var elements = document.querySelectorAll(selector);
    elements.forEach(function (el) {
      el.addEventListener("click", function () {
        pushEvent(eventName, extra || {});
      });
    });
  }

  bindClick(".js-whatsapp", "click_whatsapp", { channel: "whatsapp" });
  bindClick(".js-cta-rdv", "click_cta_rdv", { location: "landing" });
  bindClick("a[href^='mailto:']", "click_email", { channel: "email" });
  bindClick("a[href^='tel:']", "click_phone", { channel: "phone" });

  var formGuide = document.getElementById("form-guide");
  if (formGuide) {
    formGuide.addEventListener("submit", function () {
      pushEvent("submit_guide_form", { form_name: "guide" });
    });
  }

  var formDevis = document.getElementById("form-devis");
  if (formDevis) {
    formDevis.addEventListener("submit", function () {
      pushEvent("submit_devis_form", { form_name: "devis" });
    });
  }
})();
