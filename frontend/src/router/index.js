import { createRouter, createWebHistory  } from 'vue-router'
import MovieList from '../components/MovieList.vue'
import MovieDetails from '../components/MovieDetails.vue'
import AddMovie from '../components/AddMovie.vue'

const routes = [
  { path: '/', redirect: '/movies' },
  { path: '/movies', name: 'Home', component: MovieList },
  { path: '/movies/:id', name: 'MovieDetails', component: MovieDetails },
  {path: '/add', name: 'AddMovie',  component: AddMovie}

]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router