<template>
  <v-app>
    <v-app-bar color="#3248d5" app>
      <v-toolbar-title class="headline text-uppercase">
        <v-img :src="require('@/assets/unbabel-logo.svg')"></v-img>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container fluid>
          <TranslationBox v-on:add-translation="addTranslation"/>
          <TranslationList v-bind:translations="translations" v-on:del-translation="deleteTranslation"/>
      </v-container>
    </v-content>

  </v-app>
</template>

<style scoped>

</style>

<script>
import TranslationBox from './components/TranslationBox.vue';
import TranslationList from './components/TranslationList.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    TranslationBox,
    TranslationList
  },
  data() {
    return {
      translations: [],
    }
  },
  methods: {
    deleteTranslation(uid) {
      axios.delete(`http://localhost/api/translations/${uid}`);
      this.translations = this.translations.filter(translation => translation.uid !== uid);
      this.translations.sort((a, b) => b.orig_text.length - a.orig_text.length)
  },

    addTranslation(newTranslation) {
      const { orig_text, target_language, source_language, status } = newTranslation;

      axios.post("http://localhost/api/translations/", {
        orig_text,
        target_language, 
        source_language, 
        status         
      })
        .then(res => {this.translations = [...this.translations, res.data.data]})
      this.translations.sort((a, b) => b.orig_text.length - a.orig_text.length)
    },
  },
  mounted: function() {
    axios.get(`http://localhost/api/translations/`)
      .then(res => {this.translations = res.data.data})
    this.translations.sort((a, b) => b.orig_text.length - a.orig_text.length)
  },
}
</script>
