<template>
    <div class="translation-item">
        <v-expansion-panel>
            <v-expansion-panel-header disable-icon-rotate>
                <template v-slot:actions>
                    <v-icon color="green" v-if="translation.status === 'requested'">mdi-file-check-outline</v-icon>
                    <v-icon color="orange" v-if="translation.status === 'pending'">mdi-clock-outline</v-icon>
                    <v-icon color="blue" v-if="translation.status === 'translated'">mdi-check</v-icon>
                </template>
                <v-row justify="center">
                    <v-col cols="12" md="8">
                        <v-text name="trans_text">
                            <div v-if="translation.orig_text.length<25">{{translation.orig_text}}</div>
                            <div v-else>{{ translation.orig_text.substring(0,25)+".." }}</div>
                        </v-text>
                    </v-col>
                    <v-col cols="12" md="4">
                        <v-label class="status">
                            {{translation.status}}
                        </v-label>
                    </v-col>
                </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-row justify="end">
                    <v-btn icon>
                        <v-icon @click="$emit('del-translation', translation.uid)" class="del mr-3 mb-6">mdi-trash-can-outline</v-icon>
                    </v-btn>
                </v-row>
                <v-row justify="center">
                        <v-text name="english_label">(EN)</v-text>
                        <v-icon>mdi-arrow-right-bold</v-icon>
                        <v-text name="spanish_label">(ES)</v-text>
                </v-row>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
                <v-row>
                    <v-label name="english_tag">English (EN)</v-label>
                </v-row>
                <v-row>
                    <v-text name="orig-text">{{translation.orig_text}}</v-text>
                </v-row>
            </v-expansion-panel-content>
            <v-expansion-panel-content>
                <v-row>
                    <v-label name="spanish_tag">Spanish (ES)</v-label>
                </v-row>
                <v-row>
                    <v-text name="trans-lang">{{translation.trans_text}}</v-text>
                </v-row>
            </v-expansion-panel-content>
        </v-expansion-panel>
    </div>
</template>

<script>
export default {
  name: "TranslationItem",
  props: ["translation"],
  methods: {
  }
}
</script>

<style scoped>
  .v-label{
    font-size: 12px;
  }
</style>
