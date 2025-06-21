<!-- <template>
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
</template> -->

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

export default {
  name: 'MovieList',
  data() {
    return {
      movies: [],
      loading: false,
      nextPageUrl: null,
      prevPageUrl: null,
      currentUrl: 'http://127.0.0.1:8000/movies/',
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


<!-- 
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
</script> -->
