$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-homework .modal-content").html("");
        $("#modal-homework").modal("show");
      },
      success: function (data) {
        $("#modal-homework .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#homework-table tbody").html(data.html_homework_list);
          $("#modal-homework").modal("hide");
        }
        else {
          $("#modal-homework .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create homework
  $(".js-create-homework").click(loadForm);
  $("#modal-homework").on("submit", ".js-homework-create-form", saveForm);

  // Update couhomeworkrse
  $("#homework-table").on("click", ".js-update-homework", loadForm);
  $("#modal-homework").on("submit", ".js-homework-update-form", saveForm);

  // Delete homework
  $("#homework-table").on("click", ".js-delete-homework", loadForm);
  $("#modal-homework").on("submit", ".js-homework-delete-form", saveForm);

});
