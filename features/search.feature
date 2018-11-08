@Search
Feature: Search

  Scenario: login
    Given the home page open
     Then user logs in with username "bongadubula@gmail.com" and password "bonga"

     When the user search for an item
     And add item to cart 