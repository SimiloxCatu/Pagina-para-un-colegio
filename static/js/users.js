$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-user .modal-content").html("");
        $("#modal-user").modal("show");
      },
      success: function (data) {
        $("#modal-user .modal-content").html(data.html_form);
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
          $("#user-table tbody").html(data.html_user_list);
          $("#modal-user").modal("hide");
        }
        else {
          $("#modal-user .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create user
  $(".js-create-user").click(loadForm);
  $("#modal-user").on("submit", ".js-user-create-form", saveForm);

  // Update user
  $("#user-table").on("click", ".js-update-user", loadForm);
  $("#modal-user").on("submit", ".js-user-update-form", saveForm);

  // Delete user
  $("#user-table").on("click", ".js-delete-user", loadForm);
  $("#modal-user").on("submit", ".js-user-delete-form", saveForm);

});
/*
    $(function () {
      $('.apireq').click( function() {
        $.ajax({
              url : "http://localhost:8000/user?format=json",
              dataType: "json",
              success : function (data) {
                    $('#username').text( data[0].username);
                    $('#email').text( data[0].email);
                    $('#first_name').text( data[0].first_name);
                    $('#last_name').text( data[0].last_name);
                    $('#telephone').text( data[0].telephone);
                    $('#student').text( data[0].is_student);
                    $('#teacher').text( data[0].is_teacher);
                    $('#super').text( data[0].is_supervisor);
                }
            });
        });
          }); 



    <script type="text/javascript">
    </script>
<div>
   <button class="apireq">click me </button> 
</div>

<div id="jsonresp" style="margin-top: 100px">
   <p><label> Username :</label> <span id="username"></span></p>
   <p><label> Email :</label> <span id="email"></span></p>
   <p><label> First name :</label> <span id="first_name"></span></p>
   <p><label> Last name :</label> <span id="last_name"></span></p>
   <p><label> telephone :</label> <span id="telephone"></span></p>
   <p><label> Student : </label> <span id="student"></span></p> 
   <p><label> Teacher : </label> <span id="teacher"></span></p> 
   <p><label> Super : </label> <span id="super"></span></p> 
</div>*/