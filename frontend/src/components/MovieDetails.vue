<template>
  <div class="container mt-5">
    <!-- Back Button -->
    <button class="btn btn-outline-secondary mb-4" @click="$router.push('/movies')">
      &larr; Back to list
    </button>

    <!-- Loading / Error state -->
    <div v-if="!movie" class="text-center text-muted">
      <div class="spinner-border mb-3" role="status"></div>
      <p>Loading movie details...</p>
    </div>

    <!-- Movie Card -->
    <div v-else class="card shadow-sm">
      <div class="card-body">
        <!-- Title -->
        <h2 class="card-title text-primary">{{ movie.title }}</h2>
        <hr />

        <!-- Description Section -->
        <div class="mb-4">
          <h5>Description</h5>
          <div v-if="!editingDescription" class="mb-2">{{ movie.description }}</div>
          <textarea
            v-else
            v-model="editedDescription"
            class="form-control mb-2"
            rows="3"
          ></textarea>
          <button
            class="btn btn-sm btn-outline-secondary me-2"
            @click="toggleEditDescription"
          >
            {{ editingDescription ? 'Cancel' : 'Edit Description' }}
          </button>
          <button
            v-if="editingDescription"
            class="btn btn-sm btn-primary"
            @click="saveDescription"
          >
            Save
          </button>
        </div>

        <!-- Actors Section -->
        <div class="mb-4">
        <h5>Actors</h5>

        <!-- Use template to wrap v-if block -->
        <template v-if="!editingActors">
            <ul class="list-group mb-2">
            <li
                v-for="actor in movie.actors"
                :key="actor.id"
                class="list-group-item"
            >
                {{ actor.first_name }} {{ actor.last_name }}
            </li>
            </ul>
        </template>

        <!-- Use template to wrap v-else block -->
        <template v-else>
            <div class="row g-2">
            <div
                v-for="(actor, index) in editedActors"
                :key="index"
                class="col-md-6"
            >
                <input
                v-model="editedActors[index].first_name"
                type="text"
                class="form-control mb-1"
                placeholder="First Name"
                />
                <input
                v-model="editedActors[index].last_name"
                type="text"
                class="form-control"
                placeholder="Last Name"
                />
            </div>
            </div>

            <!-- Add New Actor Inputs -->
            <div class="row mt-3">
            <div class="col-md-5">
                <input
                v-model="newActor.first_name"
                type="text"
                class="form-control"
                placeholder="New Actor First Name"
                />
            </div>
            <div class="col-md-5">
                <input
                v-model="newActor.last_name"
                type="text"
                class="form-control"
                placeholder="New Actor Last Name"
                />
            </div>
            <div class="col-md-2">
                <button class="btn btn-success w-100" @click="addNewActorToList">
                Add
                </button>
            </div>
            </div>
        </template>

        <button
            class="btn btn-sm btn-outline-secondary me-2 mt-2"
            @click="toggleEditActors"
        >
            {{ editingActors ? 'Cancel' : 'Edit Actors' }}
        </button>
        <button
            v-if="editingActors"
            class="btn btn-sm btn-primary mt-2"
            @click="saveActors"
        >
            Save Actors
        </button>
        </div>

        <!-- Average Rating -->
        <div class="mb-4">
          <h5>Average Rating</h5>
          <p class="fw-bold">{{ averageRating.toFixed(2) }}</p>
        </div>

        <!-- Review Form -->
        <div class="mb-4">
          <h5>Add Review</h5>
          <select
            v-model="newReviewGrade"
            class="form-select w-auto mb-2"
          >
            <option disabled value="0">Select rating</option>
            <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
          </select>
          <button
            class="btn btn-primary"
            :disabled="newReviewGrade < 1"
            @click="submitReview"
          >
            Submit Review
          </button>
        </div>

        <!-- Reviews List -->
        <div>
          <h5>Reviews</h5>
          <ul class="list-group">
            <li
              v-for="review in movie.reviews"
              :key="review.id"
              class="list-group-item"
            >
              Rating: {{ review.grade }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from 'axios'

export default {
  name: 'MovieDetails',
  data() {
    return {
       movie: {
       title: '',
       description: '',
       actors: [],
       reviews: [],
       id: null,
    },
    editingDescription: false,
    editedDescription: '',
    editingActors: false,
    allActors: [], 
    selectedActorId: '',
    editedActors: [],
    newReviewGrade: 0,
    newActor: {
        first_name: '',
        last_name: '',
    }
    }
   
  },
  computed: {
    averageRating() {
        if (!this.movie || !this.movie.reviews || !this.movie.reviews.length) return 0;
        const total = this.movie.reviews.reduce((sum, r) => sum + r.grade, 0);
        return total / this.movie.reviews.length;
    },
  },
  methods: {
    fetchMovie() {
      const id = this.$route.params.id
      axios.get(`http://127.0.0.1:8000/movies/${id}/`)
        .then(res => {
          this.movie = res.data
          this.editedDescription = this.movie.description
          this.editedActors = JSON.parse(JSON.stringify(this.movie.actors))
        })
        .catch(err => console.error(err))
    },
    toggleEditDescription() {
      if (!this.movie) return
      this.editingDescription = !this.editingDescription
      this.editedDescription = this.movie.description
    },
    saveDescription() {
      axios.patch(`http://127.0.0.1:8000/movies/${this.movie.id}/`, {
        description: this.editedDescription
      })
      .then(() => {
        this.movie.description = this.editedDescription
        this.editingDescription = false
      })
      .catch(err => console.error(err))
    },
    toggleEditActors() {
      this.editingActors = !this.editingActors
      this.editedActors = JSON.parse(JSON.stringify(this.movie.actors))
    },
    addNewActorToList() {
    if (this.newActor.first_name.trim() && this.newActor.last_name.trim()) {
        this.editedActors.push({
        first_name: this.newActor.first_name,
        last_name: this.newActor.last_name,
        id: null // means this actor is new
        })
        this.newActor.first_name = ''
        this.newActor.last_name = ''
    }
    },
    
    async saveActors() {
        const actorIds = []
        for (const actor of this.editedActors) {
        if (actor.id) {
            // Existing actor
            actorIds.push(actor.id)
        } else {
            // New actor ? save it to DB
            const res = await axios.post('http://127.0.0.1:8000/actors/', {
            first_name: actor.first_name,
            last_name: actor.last_name
            })
            actorIds.push(res.data.id)
        }
      }
      axios.patch(`http://127.0.0.1:8000/movies/${this.movie.id}/`, {
        actors: this.editedActors.map(actor => actor.id)
      })
      .then(() => {
        this.movie.actors = JSON.parse(JSON.stringify(this.editedActors))
        this.editingActors = false
      })
      .catch(err => console.error(err))
    },
    cancelEditActors() {
      this.editingActors = false
    },
    submitReview() {
      axios.post(`http://127.0.0.1:8000/reviews/`, {
        grade: this.newReviewGrade,
        movie: this.movie.id
      })
      .then(res => {
        this.movie.reviews.push(res.data)
        this.newReviewGrade = 0
      })
      .catch(err => console.error(err))
    }
  },
  mounted() {
    this.fetchMovie()
  }
}
</script>
