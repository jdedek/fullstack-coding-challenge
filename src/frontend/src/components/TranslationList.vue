 <template>
    <div class="translation-list mb-6 ">
        <v-row justify="center">
            <v-col cols="12" md="6">
                <v-text name="translation-list-header">
                    My Translations:
                </v-text>
            </v-col>
        </v-row>
        <v-expansion-panels v-bind:key="translation.uid" v-for="translation in translations" >
            <v-col cols="12" md="6">
                <TranslationItem v-bind:translation="translation" v-on:del-translation="$emit('del-translation', translation.uid)"/>
            </v-col>
        </v-expansion-panels>
    </div>
 </template>

 <script>
import TranslationItem from "./TranslationItem.vue"

export default {
    name: 'TranslationList',
    components: {
        TranslationItem
    },
    props: ["translations"]
}
 </script>


 <style scoped>

 </style>