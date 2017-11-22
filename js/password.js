function pass() {
    var pass_1 = document.forms["passwordForm"].password.value;
    var correct_pass = "password"
    if (pass_1 == correct_pass) {
        window.location.replace("secret_resources.html");
    } else {
      alert("try again it's wrong");
    }
    return true;
}
