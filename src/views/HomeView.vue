<script setup>

</script>

<template>
  <main class="welcome">
    <h1>Welcome to Dragon Ball world</h1>
    <img src="https://www.gratistodo.com/wp-content/uploads/2017/02/dragones-19.gif" alt="welcome">
  </main>
</template>

<style scoped>
.welcome {
  color: aliceblue;
  display: ruby;
}

.welcome img {
  transition: box-shadow 0.9s ease;
  border-radius: 15px;
  width: 63%;
}

.welcome img:hover {
  box-shadow: 0px 0px 50px rgba(255, 13, 0, 0.788);
}

h1 {
  margin: 15px;
  font-size: 3rem;
  color: #ff4500;
  text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500, 0 0 40px #ff4500, 0 0 50px #ff4500, 0 0 60px #ff4500, 0 0 70px #ff4500;
  animation: flame 3s infinite alternate;
}

@keyframes flame {
  0% {
    color: #ff4500;
    text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500, 0 0 40px #ff4500, 0 0 50px #ff4500, 0 0 60px #ff4500, 0 0 70px #ff4500;
  }

  25% {
    color: #ff6347;
    text-shadow: 0 0 20px #ff6347, 0 0 30px #ff6347, 0 0 40px #ff6347, 0 0 50px #ff6347, 0 0 60px #ff6347, 0 0 70px #ff6347;
  }

  50% {
    color: #ff7f50;
    text-shadow: 0 0 20px #ff7f50, 0 0 30px #ff7f50, 0 0 40px #ff7f50, 0 0 50px #ff7f50, 0 0 60px #ff7f50, 0 0 70px #ff7f50;
  }

  75% {
    color: #ffa07a;
    text-shadow: 0 0 20px #ffa07a, 0 0 30px #ffa07a, 0 0 40px #ffa07a, 0 0 50px #ffa07a, 0 0 60px #ffa07a, 0 0 70px #ffa07a;
  }

  100% {
    color: #ff4500;
    text-shadow: 0 0 20px #ff4500, 0 0 30px #ff4500, 0 0 40px #ff4500, 0 0 50px #ff4500, 0 0 60px #ff4500, 0 0 70px #ff4500;
  }
}
</style>
