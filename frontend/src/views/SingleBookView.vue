<template>
  <div class="single-book">
    <template v-if="book">
      <h1>{{ book.title }}</h1>
      <v-btn flat @click="handleEditClick">Edit</v-btn>
      <v-btn flat @click="handleDeleteClick">Delete</v-btn>
      <h2 class="mt-2">Written by {{ book.author }}</h2>
      <p class="mt-3">Rated {{ book.rating }} out of 5</p>
    </template>
  </div>
</template>

<script>
export default {
  name: 'SingleBooksView',
  data() {
    return {
      book: null
    };
  },
  computed: {
    bookId() {
      return this.$route.params.bookId;
    },
  },
  created(){
    this.getSingleBook();
  },
  methods: {
    async getSingleBook(){
      const bookResponse = await fetch(`http://localhost:5000/books/${this.bookId}`);
      const bookJson = await bookResponse.json();
      this.book = bookJson;
    }
    handleEditClick() {
      this.$router.push(`/books/${this.book.bookId}/edit`);
    },
    handleDeleteClick() {
      this.$router.push('/books');
    },
  },
};
</script>
