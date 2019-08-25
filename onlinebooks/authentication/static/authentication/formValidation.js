$("#id_email").change(function () {
    var email = $(this).val();
    var emailRegex = /^[a-z0-9.%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/i;
    if (!emailRegex.test(email)) {
        let emailAlert = '<span class="text-danger" id="email-error-message">Please enter a valid email address</span>';
        $(this).parent().append(emailAlert);
        return;
    }
    checkAvailableEmail(email);
});

$('#id_email').on("input focus", function () {
    if ($('#email-error-message').length) {
        $("#email-error-message").remove();
    }
    if ($('#email-exists-message').length) {
        $("#email-exists-message").remove();
    }
});

$("[type=password]").change(function(){
    var password1 = $("#id_password1").val();
    var password2 = $("#id_password2").val();
    if(password1 !== password2)
    {
        let passwordNotMatchAlert = '<span class="text-danger" id="password-mismatch-error-message">The two passwords don\'t match</span>'
        $('#id_password2').parent().append(passwordNotMatchAlert);
    }
});

$("[type=password]").focus(function(){
    if($("#password-mismatch-error-message").length)
    {
        $("#password-mismatch-error-message").remove();
    }
});

$("#id_mobile_no_0, #id_mobile_no_1").change(function(){
    var mobile_no_0 = $("#id_mobile_no_0").val();
    var mobile_no_1 = $("#id_mobile_no_1").val();
    var mobileRegex = /[0-9]{1,10}/;
    if(!mobileRegex.test(mobile_no_0) && mobile_no_0 !== "" && !($("#country-code-error-message").length))
    {
        let countryCodeErrorMessage = '<span class="text-danger" id="country-code-error-message">Please enter a valid country code</span>';
        $("#id_mobile_no_0").parent().append(countryCodeErrorMessage);
    }
    if(!mobileRegex.test(mobile_no_1) && mobile_no_1 !== "" &&  !($("#mobile-no-error-message").length))
    {
        console.log(mobile_no_1);
        let mobileNumberErrorMessage = '<span class="text-danger" id="mobile-no-error-message">Please enter a valid mobile number</span>';
        $("#id_mobile_no_1").parent().append(mobileNumberErrorMessage);
    }
});

$("#id_mobile_no_0, #id_mobile_no_1").on("input focus", function(){
    $(this).siblings('span').remove();
});

$("#signUpForm").submit(function(e){
    e.preventDefault();
    var form = this;
    if(checkAvailableEmail($("#id_email").val()))
    {
        form.submit();
    }
})

function checkAvailableEmail(email){
    var returnValue = true;
    $.get("/authenticate/ajax/", { 'email': email })
        .done(function (data) {
            if (data["exists"]) {
                let emailRegisteredAlert = '<span class="text-danger" id="email-exists-message">The email address is already registered with us</span>';
                $("#id_email").parent().append(emailRegisteredAlert);
                returnValue = false;
            }
        });
    return returnValue;    
}
