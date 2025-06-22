<template>
  <nav class="navbar navbar-expand-lg" style="background-color: black;">
    <div class="container">
      <router-link class="navbar-brand" to="/movies" style="color: white;">Movie App</router-link>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ms-auto">
            <li class="nav-item">
            <router-link class="btn btn-primary me-2" to="/movies">Home</router-link>
            </li>
            <li class="nav-item">
            <button class="btn btn-success" @click="$router.push('/add')">Add New Movie</button>
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
