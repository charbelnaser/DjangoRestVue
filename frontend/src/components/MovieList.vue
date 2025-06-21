
<template>
  <div class="container mt-4">
    <h2>Movies</h2>

    <div v-if="loading" class="text-muted">Loading...</div>

    <ul class="list-group mb-3" v-else>
      <li v-for="movie in movies" :key="movie.id" class="list-group-item">
        <router-link :to="`/movies/${movie.id}`">{{ movie.title }}</router-link>
      </li>
    </ul>

    <!-- Pagination Controls -->
    <nav v-if="pageCount > 1">
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: !prevPageUrl }">
          <button class="page-link" @click="changePage(prevPageUrl)">Previous</button>
        </li>
        <li class="page-item" :class="{ disabled: !nextPageUrl }">
          <button class="page-link" @click="changePage(nextPageUrl)">Next</button>
        </li>
      </ul>
    </nav>
  </div>
</template>


<script>
import axios from 'axios';
const API_URL = process.env.VUE_APP_API_URL || 'http://127.0.0.1:8000';
export default {
  name: 'MovieList',
  data() {
    return {
      movies: [],
      loading: false,
      nextPageUrl: null,
      prevPageUrl: null,
      currentUrl: `${API_URL}/movies/`,
    };
  },
  computed: {
    pageCount() {
      return this.nextPageUrl || this.prevPageUrl ? 2 : 1;
    },
  },
  methods: {
    fetchMovies(url = this.currentUrl) {
      this.loading = true;
      axios.get(url)
        .then((res) => {
          this.movies = res.data.results;
          this.nextPageUrl = res.data.next;
          this.prevPageUrl = res.data.previous;
        })
        .catch((err) => console.error(err))
        .finally(() => {
          this.loading = false;
        });
    },
    changePage(url) {
      if (url) {
        this.fetchMovies(url);
      }
    }
  },
  mounted() {
    this.fetchMovies();
  }
};
</script>
