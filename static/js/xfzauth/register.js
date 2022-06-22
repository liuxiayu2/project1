// 注册
$(function () {
    var usernameInput = $('input[class="login_name"]');
    var telInput = $('input[class="login_tel"]');
    var passwdInput = $('input[class="login_passwd"]');
    var passwdInput1 = $('input[class="login_passwd1"]');
    var submitBtn = $('.register_btn');
    // console.log(submitBtn);

    submitBtn.click(function (event) {
        event.preventDefault();
        var username = usernameInput.val(),
            telephone = telInput.val(),
            password = passwdInput.val(),
            password1 = passwdInput1.val();
        console.log(password);
        // $('#form').submit();
        $.ajax({
            type:"POST",
            url:"",
            data:{
                username:username,
                telephone:telephone,
                password:password
            },
            success:function () {
                window.location.href='/'
            }
            }
        )
        console.log('password');
    });
})