 <template>
    <div class="translation-list">

        <v-row justify="center">
            <v-col cols="12" md="6">
                <v-text name="translation-list-header">
                    My Translations:
                </v-text>
            </v-col>
        </v-row>

        <v-row justify="center">
            <v-col cols="12" md="6">
                <v-expansion-panels>
                    
                    <v-expansion-panel>
                    
                        <v-expansion-panel-header>
                            <v-row justify="center">
                                <v-col cols="12" md="8">
                                    <v-text name="trans_text">
                                        Lorem ipsum dolor sit amet...
                                    </v-text>            
                                </v-col>
                                
                                <v-col cols="12" md="4">
                                    <v-badge color="green">
                                        <template v-slot:badge>
                                            <v-icon>mdi-check</v-icon>
                                        </template>
                                        <span>
                                            requested
                                        </span>
                                    </v-badge>           
                                </v-col>
                            </v-row>
                        </v-expansion-panel-header>
          
                        <v-expansion-panel-content>
                            <v-row justify="center">
                                <v-text name="english_tag">
                                    English (EN)
                                </v-text>
                                <v-btn icon>
                                    <v-icon class="ma-0 pa-0">mdi-arrow-right-bold</v-icon>
                                </v-btn>
                                <v-text name="spanish_tag">
                                    Spanish (ES)
                                </v-text>
                            </v-row>
                        </v-expansion-panel-content>
                        
                        <v-expansion-panel-content>
                            <v-text name="english_trans">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                            </v-text>
                        </v-expansion-panel-content>

                        <v-expansion-panel-content>
                            <v-text name="spanish_trans">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                            </v-text>
                        </v-expansion-panel-content>
        
                    </v-expansion-panel> 
                </v-expansion-panels>
            </v-col>
        </v-row>   
    </div>
 </template>

 <script>
export default {
    name: 'TranslationList',
    props: ["translations"]
}
 </script>


 <style scoped>

 </style>