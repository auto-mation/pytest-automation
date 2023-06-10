Feature: appointments reservation

  Background:
    Given user navigate to home page

  @gui
  Scenario Outline: A user reserve an appointment 
    Then user login with username "John Doe" and password "ThisIsNotAPassword"
    When user navigate to appointments page
    Then user set Facility "<facility>"
    Then user set hospital readmission "<readmission>"
    Then user set Healthcare Program "<program>"
    Then user set Visit date "<date>"
    Then user set Comment "<comment>"
    When user click Book Appointment
    Then user navigate to history page
    Then user find appointment with date "<date>" and Facility "<facility>" and Program "<program>"
    Then user logout
  Examples:
        | facility | readmission | program | date |  comment |
        | Hongkong CURA Healthcare Center | True | Medicaid | CURRENT_DATE | | 
        | Tokyo CURA Healthcare Center | False | None | 11/12/2023 | N/A | 
        | Seoul CURA Healthcare Center | True | Medicare | 22/09/2023 | I want the slot after 7PM with doctor John.| 
        