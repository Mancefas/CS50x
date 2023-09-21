-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Checking how the database looks and what data can i get
.schema

-- Checking the report on date that the theft took place and the street it took place in
SELECT description
    FROM crime_scene_reports
        WHERE month = 7 AND day = 28
        AND street = 'Humphrey Street';
-- FROM REPORTS - Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

-- Lets look at the interviews and search for those 3 interviews
SELECT name, transcript FROM interviews
    WHERE month = 7 AND day = 28 AND transcript like  '%bakery%';

-- | Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- 1st checking info from Ruth interview
-- looked at crime_scene_reports again and the time that crime took place is at 10:15AM
.tables bakery_security_logs
-- looking activity and license_plate at that time +10min
SELECT people.name as suspects_from_security_logs
    FROM bakery_security_logs
    JOIN people ON people.license_plate = bakery_security_logs.license_plate
    WHERE month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = 'exit'
    ORDER BY people.name;

-- +-----------------------------+
-- | suspects_from_security_logs |
-- +-----------------------------+
-- | Barry                       |
-- | Bruce                       |
-- | Diana                       |
-- | Iman                        |
-- | Kelsey                      |
-- | Luca                        |
-- | Sofia                       |
-- | Vanessa                     |
-- +-----------------------------+

-- 2nd checking Eugene interview
.schema atm_transactions

-- need to check who took out money in the morning
SELECT people.name as suspect_from_ATM
    FROM atm_transactions
    JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
    JOIN people ON people.id = bank_accounts.person_id
    WHERE month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'
    ORDER BY people.name;

-- +------------------+
-- | suspect_from_ATM |
-- +------------------+
-- | Benista          |
-- | Brooke           |
-- | Bruce            | +
-- | Diana            | +
-- | Iman             | +
-- | Kenny            |
-- | Luca             | +
-- | Taylor           |
-- +------------------+

-- 3nd checking Raymond interview

SELECT calling_person.name as caller, receiving_call_person.name as receiver
    FROM phone_calls
    JOIN people as calling_person ON calling_person.phone_number = phone_calls.caller
    JOIN people as receiving_call_person ON receiving_call_person.phone_number = phone_calls.receiver
    WHERE month = 7 AND day = 28 AND duration < 60
    ORDER BY caller, receiver;

-- +---------+------------+
-- | caller  |  receiver  |
-- +---------+------------+
-- | Benista | Anna       |
-- | Bruce   | Robin      | +
-- | Carina  | Jacqueline |
-- | Diana   | Philip     | +
-- | Kelsey  | Larry      |
-- | Kelsey  | Melissa    |
-- | Kenny   | Doris      |
-- | Sofia   | Jack       |
-- | Taylor  | James      |
-- +---------+------------+

SELECT destination.city as flying_to, people.name as suspect
    FROM flights
    JOIN airports as destination ON destination.id = flights.destination_airport_id
    JOIN airports as origin ON origin.id = flights.origin_airport_id
    JOIN passengers ON passengers.flight_id = flights.id
    JOIN people ON people.passport_number = passengers.passport_number
    WHERE month = 7 AND day = 29 AND origin.city = 'Fiftyville'
    ORDER BY hour
    LIMIT 5;

-- +---------------+---------+
-- |   flying_to   | suspect |
-- +---------------+---------+
-- | New York City | Doris   |
-- | New York City | Sofia   |
-- | New York City | Bruce   | +
-- | New York City | Edward  |
-- | New York City | Kelsey  |
-- +---------------+---------+
