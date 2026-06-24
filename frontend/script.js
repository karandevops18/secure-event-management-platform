const API_URL = "http://192.168.1.8:5000/api";

async function registerUser() {

    const name =
        document.getElementById("reg-name").value;

    const email =
        document.getElementById("reg-email").value;

    const password =
        document.getElementById("reg-password").value;

    const response = await fetch(
        `${API_URL}/register`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                email,
                password
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").innerHTML =
        JSON.stringify(data);
}


async function loginUser() {

    const email =
        document.getElementById("login-email").value;

    const password =
        document.getElementById("login-password").value;

    const response = await fetch(
        `${API_URL}/login`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").innerHTML =
        JSON.stringify(data);
}