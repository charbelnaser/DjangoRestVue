<template>
  <nav class="navbar navbar-expand-lg" style="background-color: black;">
    <div class="container">
      <a class="navbar-brand" href="#" style="color: white;">Movie App</a>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ms-auto">
            <li class="nav-item">
            <router-link class="btn btn-primary me-2" to="/">Home</router-link>
            </li>
            <li class="nav-item">
            <router-link class="btn btn-primary" to="/add">Add Movie</router-link>
            </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>
