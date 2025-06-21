<template>
  <div class="container mt-5">
    <h2>Add New Movie</h2>

    <!-- Movie Title -->
    <div class="mb-3">
      <input v-model="movie.title" class="form-control" placeholder="Movie Title" />
    </div>

    <!-- Movie Description -->
    <div class="mb-3">
      <textarea v-model="movie.description" class="form-control" placeholder="Movie Description"></textarea>
    </div>

    <!-- Select Actors -->
    <div class="mb-3">
      <label>Select Actors:</label>
        <select v-model.number="selectedActorId" class="form-select">
        <option disabled value="">Choose actor</option>
        <option v-for="actor in allActors" :key="actor.id" :value="actor.id">
          {{ actor.first_name }} {{ actor.last_name }}
        </option>
      </select>
      <button class="btn btn-outline-primary mt-2" @click="addActor">Add Actor</button>

      <ul class="list-group mt-2">
        <li v-for="actor in selectedActors" :key="actor.id" class="list-group-item d-flex justify-content-between align-items-center">
            {{ actor.first_name }} {{ actor.last_name }}
            <button class="btn btn-sm btn-danger" @click="removeActor(actor.id)">Remove</button>
        </li>
       </ul>
    </div>

    <!-- Initial Review -->
    <div class="mb-3">
      <label>Add a Review (1-5):</label>
      <select v-model="initialReview" class="form-select w-auto">
        <option disabled value="">Select grade</option>
        <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
      </select>
    </div>

    <button class="btn btn-success" @click="submitMovie">Create Movie</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddMovie',
  data() {
    return {
      movie: {
        title: '',
        description: ''
      },
      selectedActorId: '',
      allActors: [],
      selectedActors: [],
      initialReview: ''
    };
  },
  methods: {
    fetchActors() {
      axios.get('http://127.0.0.1:8000/actors/')
        .then(res => {
            
          this.allActors = res.data.results;
         

        })
        .catch(err => console.error(err));
    },
    addActor() {
        if (!this.selectedActorId) return;  // Don't do anything if nothing is selected

        const actor = this.allActors.find(a => a.id === this.selectedActorId);

        if (actor && !this.selectedActors.some(a => a.id === actor.id)) {
            this.selectedActors.push(actor);
        }

        this.selectedActorId = '';  // Reset selection
    },
    removeActor(id) {
      this.selectedActors = this.selectedActors.filter(actor => actor.id !== id);
    },
    async submitMovie() {
      try {
        // 1. Create movie
        const movieRes = await axios.post('http://127.0.0.1:8000/movies/', {
          title: this.movie.title,
          description: this.movie.description,
          actors: this.selectedActors.map(actor => actor.id)
        });

        const movieId = movieRes.data.id;

        // 2. Submit initial review (optional)
        if (this.initialReview) {
          await axios.post('http://127.0.0.1:8000/reviews/', {
            grade: this.initialReview,
            movie: movieId
          });
        }

        // 3. Redirect to movie list
        this.$router.push('/movies');
      } catch (err) {
        console.error(err);
        alert('Failed to create movie');
      }
    }
  },
  mounted() {
    this.fetchActors();
  }
};
</script>
