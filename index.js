options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    username: "Avani02",
    password: "Avani02*",
  }),
};

async function setToken() {
  const response = await fetch("http://65.20.89.184/api/login/", options);
  const data = await response.json();
  await localStorage.setItem("access", data.token.access);

  socket = new WebSocket("ws://65.20.89.184:8888/");
  socket.onopen = function () {
    console.log("Connected");
    socket.send(localStorage.getItem("access"));
  };
  socket.onmessage = function (e) {
    console.log(e.data);
  };

  socket.onclose = function () {
    console.log("Disconnected");
  };
  
  return socket
}

const hello = setToken();