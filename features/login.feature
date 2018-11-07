Feature: Login

  Scenario: successful login
    Given the home page is open
     Then the user logs in with username "bongadubula@gmail.com" and password "bonga"
     #Then the message "You logged out of the secure area!" is shown

  Scenario: successful logout
    Given the home page is open
     Then the user logs in with username "bongadubula@gmail.com" and password "bonga"
      Then the user logs out
     #Then the message "You logged out of the secure area!" is shown
