<template>
  <div class="container mt-4">
    <h1 class="text-dark">Movies</h1>
    <div class="row">
      <div class="col-md-4 mb-3" v-for="movie in movies" :key="movie.id">
        <div class="card h-100">
          <div class="card-body text-dark">
            <h5 class="card-title">
              <router-link :to="`/movies/${movie.id}`"  class="text-dark">{{ movie.title }}</router-link>
            </h5>
            <p class="card-text text-dark">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieList',
  data() {
    return {
      movies: []
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/movies/')
      .then(res => {
        this.movies = res.data  // Directly use the list
      })
      .catch(err => {
        console.error('Failed to load movies:', err)
      })
  }
}
</script>
