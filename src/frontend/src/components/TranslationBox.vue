 <template>
    <div class="translation-box">
        <v-container fluid>
            <v-row justify="center">
                <v-text name="english_tag">English (EN)</v-text>
                <v-icon>mdi-arrow-right-bold</v-icon>
                <v-text name="spanish_tag">Spanish (ES)</v-text>
            </v-row>
        </v-container>
        <v-row justify="center">
          <v-col cols="12" md="6">
            <v-textarea
              v-model="orig_text"
              clearable
              solo
              auto-grow
              counter="10000"
              name="input-7-4"
              label="Type or paste text here..."
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row justify="center">
            <v-btn @click="addTranslation" class="mb-12" color="#3248d5" tile dark elevation=5>Submit</v-btn>
        </v-row>    
    </div>
 </template>

 <script>
export default {
  name: 'TranslationBox',
  data() {
    return{
      orig_text: ""
    }
  },
  methods: {
    addTranslation(){
      const newTranslation = {
          orig_text: this.orig_text,
          trans_text: "",
          target_language: "es",
          source_language: "en",
          status: "requested",
      }
      this.$emit("add-translation", newTranslation);
      
      // Clears the textarea
      this.orig_text = "";
    }
  }
}

 </script>


 <style scoped>


 </style>