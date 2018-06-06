function pass() {
    var pass_1 = document.forms["passwordForm"].password.value;
    var correct_pass_hash = "20c1ef2d7a61850be949d3fb6d838b75"
    if (hex_md5(pass_1) == correct_pass_hash) {
        window.location.replace("secret_resources.html");
    } else {
      alert("try again it's wrong");
    }
    return true;
}
