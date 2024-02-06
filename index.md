---
layout: default
search_exclude: true
---
-----------------------------------------------------------------------------------------------
<html lang="{{ page.lang | default: site.lang | default: " en" }}">
 
<html lang="en">
<head>
  <style>
    form {
      background-color:aqua ;
    }
    </style>
</head>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="your_stylesheet.css">
  <title>Login Page</title>
</head>
<body>
  <div class="container" style="text-align: center;">
    <h1>Nice to see you on Arushi's Blog!</h1>
    <input id="usernameInput" type="text" class="input-text" placeholder="Username">
    <input id="passwordInput" type="password" class="input-text" placeholder="Password">
    <button id="loginButton" class="button" onclick="loginUser()">Login</button>
    <button id="registerButton" class="button register-button" onclick="showRegistrationForm()">Register New User</button>

   
  <div id="registrationForm" style="display: none;">
      <h2>Register New User</h2>
      <input id="newUsernameInput" type="text" class="input-text" placeholder="New Username">
      <input id="newPasswordInput" type="password" class="input-text" placeholder="New Password">
      <button id="registerNewUserButton" class="button" onclick="registerUser()">Register</button>
    </div>
  </div>
</head>
<body>
      <script>
        function showRegistrationForm() {
      document.getElementById("registrationForm").style.display = "block";
    }
      function registerUser() {
      const newUsername = document.getElementById("newUsernameInput").value;
      const newPassword = document.getElementById("newPasswordInput").value;
    // Make a POST request to register a new user
      fetch('http://127.0.0.1:8086/api/users/authenticate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: newUsername,
          password: newPassword,
        }),
      })
      .then(response => response.json())
      .then(data => {
        console.log('User registration successful:', data);
        alert('Registration successful!');
        // Optionally, you can show a success message or redirect the user
      })
      .catch(error => {
        console.error('Error registering user:', error);
        alert('Registration failed. Please try again.');
        // Handle error, show error message, etc.
      });
    }
        const apiUrl = "http://127.0.0.1:8086/api/users/authenticate";
          document.getElementById("authenticate").onsubmit = async function (e) {
          e.preventDefault();
          const uid = document.getElementById("uid").value;
          const password = document.getElementById("password").value;
          const obj = { uid: uid, password: password };
          try {
            const response = await fetch(apiUrl, {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify(obj)
            });
            var myHeaders = new Headers();
            myHeaders.append("Content-Type", "application/json");
              var raw = JSON.stringify({
                "uid": "toby",
                "password": "123toby"
              });
              var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: raw,
                redirect: 'follow'
              };
              fetch("http://127.0.0.1:8086/api/users/authenticate", requestOptions)
                .then(response => response.text())
                .then(result => console.log(result))
                .catch(error => console.log('error', error));
            if (!response.ok) {
              throw new Error('Authentication was not successful');
            }
            const token = await response.text();
            if (token) {
              // Authentication was successful, you can handle the token as needed
              console.log('Authentication successful');
              document.cookie = `token=${token}; path=/`;
              localStorage.setItem("token", token);
              localStorage.setItem("flagData", 1);
              window.location.href = "./";
              window.location.replace("./");
            } else {
              // Authentication failed, show an error message or take appropriate action
              console.error('Authentication failed');
            }
          } catch (error) {
            console.error('Error:', error);
          }
        }
      </script>
    </div>
  </main>
</body>

</html> 


