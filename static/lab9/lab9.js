function openGift(id) {
    fetch(OPEN_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({id: id})
    })
    .then(response => response.json())
    .then(data => {

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("opened").innerText = data.opened;
        document.getElementById("remaining").innerText = data.remaining;

        document.getElementById("modal-text").innerText = data.message;
        document.getElementById("modal-image").src = "/static/lab9/" + data.image;

        document.getElementById("modal").style.display = "flex";

        document.querySelectorAll(".gift")[id].classList.add("opened");
    });
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}