@Purchasing
Feature: Buying item

  Scenario: Process of buying an item
    Given site home page is open
     When user logs with username "bongadubula@gmail.com" and password "bonga"

     And the user hovers over dresses and select dress choice
     And the user add item to cart
     Then the user checkout 