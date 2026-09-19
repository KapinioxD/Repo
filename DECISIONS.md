---
svcdesk_decisions:
  C1: wallclock
  C2: reopen
  C3: matrix
---
<!-- ai-generated: 0% - written by hand -->

# Decisions

## C1 - SLA clock for P1
**Decision:** Zegar SLA dla P1 biegnie nieprzerwanie 24 godziny na dobę, 7 dni w tygodniu (wallclock).
**Rejected alternative:** Odrzucono wariant wstrzymywania zegara P1 poza godzinami pracy.
**Reason:** Awarie krytyczne (P1) wymagają natychmiastowej reakcji firmy przez cały tydzień, bez czekania na poniedziałek.
**Service owner:** Vice President of Engineering
**Customer outcome:** Gwarancja ciągłości kluczowych usług dla całej firmy, nawet w weekendy.

## C2 - Closed tickets and reopening
**Decision:** Zgłaszający ma możliwość ponownego otwarcia zgłoszenia o statusie "closed" w ciągu 7 dni.
**Rejected alternative:** Odrzucono traktowanie stanu "closed" jako ostatecznego i niezmiennego.
**Reason:** Często zdarza się, że problem pozornie rozwiązany wraca po kilku dniach. Wznowienie zgłoszenia unika duplikatów w systemie.
**Service owner:** IT Service Desk Manager
**Customer outcome:** Wygodniejsza i szybsza obsługa bez konieczności opisywania powracającego problemu od nowa.

## C3 - VIP reporters and the priority matrix
**Decision:** O priorytecie decyduje wyłącznie obiektywna macierz. Flaga VIP nie podnosi sztucznie priorytetu.
**Rejected alternative:** Odrzucono wymuszanie priorytetu P2 dla wszystkich problemów zgłaszanych przez VIP.
**Reason:** Ograniczone zasoby Service Desku muszą być alokowane na podstawie faktycznego wpływu awarii na firmę, a nie stanowiska zgłaszającego.
**Service owner:** Chief Operating Officer
**Customer outcome:** Stabilność operacyjna całej firmy dzięki obiektywnemu priorytetyzowaniu krytycznych problemów.