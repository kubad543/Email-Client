# Prosty Klient Poczty

Prosty klient poczty e-mail stworzony w Pythonie z wykorzystaniem biblioteki Tkinter do interfejsu graficznego. Aplikacja obsługuje podstawowe funkcje związane z zarządzaniem pocztą e-mail, w tym logowanie, wysyłanie wiadomości, przeglądanie skrzynki odbiorczej oraz automatyczne odpowiadanie na odczytane wiadomości.

## Zakres Projektu

Aplikacja została zaprojektowana z myślą o prostocie obsługi oraz czytelnym interfejsie. Projekt obejmuje:

- **Logowanie do konta Gmail**: uwzględniono obsługę bezpiecznego połączenia z serwerem SMTP i IMAP.
- **Wysyłanie wiadomości e-mail**: możliwość wysyłania wiadomości do dowolnego odbiorcy z poziomu interfejsu aplikacji.
- **Przeglądanie skrzynki odbiorczej**: lista wiadomości wyświetlana w przejrzysty sposób z opcją filtrowania po słowie kluczowym.
- **Odczytywanie wiadomości**: szczegóły wiadomości (nadawca, temat, treść) wyświetlane w osobnym oknie.
- **Automatyczne odpowiadanie na wiadomości**: po odczytaniu wiadomości aplikacja automatycznie wysyła odpowiedź z informacją o przeczytaniu wiadomości.

## Kluczowe Funkcjonalności

- **Bezpieczne połączenie**: wykorzystanie protokołów SSL/TLS dla połączeń SMTP i IMAP.
- **Interfejs graficzny**: intuicyjny GUI zbudowany w oparciu o Tkinter.
- **Obsługa filtrów**: możliwość wyszukiwania wiadomości po słowie kluczowym w tytule lub treści.
- **Automatyzacja**: automatyczne generowanie odpowiedzi po odczytaniu wiadomości, co pozwala na szybkie potwierdzenie odbioru e-maili.
- **Obsługa błędów**: zaimplementowane podstawowe mechanizmy obsługi błędów przy logowaniu, wysyłaniu wiadomości oraz połączeniu z serwerami pocztowymi.

## Struktura Aplikacji

- **Interfejs użytkownika (GUI)**: pola logowania, formularz do tworzenia wiadomości, lista wiadomości odbiorczych, osobne okna do podglądu wiadomości.
- **Logika aplikacji**: obsługa połączeń SMTP i IMAP, zarządzanie sesją logowania, automatyczne odpowiedzi.
- **Bezpieczeństwo**: dane logowania przesyłane przez bezpieczne połączenie, bez lokalnego zapisu danych wrażliwych.

## Przykład Działania

1. Użytkownik loguje się do konta Gmail, podając adres e-mail i hasło.
2. Po zalogowaniu wyświetlana jest lista najnowszych wiadomości e-mail.
3. Kliknięcie przycisku **Odczytaj** otwiera nowe okno z treścią wiadomości.
4. Po odczytaniu wiadomości automatycznie generowana jest odpowiedź do nadawcy z potwierdzeniem odbioru.

## Technologie

- **Python 3.x**
- **Tkinter** – interfejs graficzny
- **smtplib** – obsługa wysyłania wiadomości (SMTP)
- **imaplib** – obsługa pobierania wiadomości (IMAP)
- **email** – parsowanie i tworzenie wiadomości e-mail

