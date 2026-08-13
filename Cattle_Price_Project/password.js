function checkPassword(){
    const password = document.getElementById("password").value;
    if(password === "Safar@17") {
        window.location.href = "index/SOURCE CODE index.html";
    }
    else {
        document.getElementById("message").innerHTML = "Incorrect password. Try again.";
    }
}
