## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## get zoom
* get_zoom
  - slot{"person": "pavan"}
  - zoom_link
  
## get zoom
* get_zoom
  - slot{"person": "datta"}
  - zoom_link

## get zoom
* get_zoom
  - zoom_link
  - slot{"person": "sanjay"}
  
## get zoom
* get_zoom
  - zoom_link
  - slot{"person": "sujith"}

## get zoom
* get_zoom
  - zoom_link
  - slot{"person": "srikanth"}

  
## get zoom
* get_zoom
  - zoom_link
  - slot{"person": "gary"}

  
## get junit
* get_junit
  - utter_junit
 
## get premerge
* get_premerge
  - utter_premerge
## interactive_story_1
* greet
    - utter_greet
* get_zoom{"person": "datta"}
    - slot{"person": "datta"}
    - zoom_link
    - slot{"person": "datta"}
* get_zoom{"person": "Datta"}
    - slot{"person": "Datta"}
    - zoom_link
    - slot{"person": "Datta"}
* get_zoom{"person": "Datta"}
    - slot{"person": "Datta"}
    - zoom_link
    - slot{"person": "Datta"}
* get_zoom{"person": "Gary"}
    - slot{"person": "Gary"}
    - zoom_link
    - slot{"person": "Gary"}
* get_zoom{"person": "Sujith"}
    - slot{"person": "Sujith"}
    - zoom_link
    - slot{"person": "Sujith"}
* stop
