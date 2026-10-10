---
actual_minutes: 150
---
# Replikacja badania METR (n=1)

Niniejszy dokument zawiera wnioski z przeprowadzonej analizy i implementacji. Głównym zadaniem w tym laboratorium było napisanie kodu obliczającego metryki DORA zgodnie z rygorystyczną specyfikacją. Początkowe estymacje zakładały szybką implementację, jednakże liczne problemy z formatowaniem, walidacją ustrukturyzowanych danych wejściowych (JSON/JSONL) oraz środowiskiem testowym i systemem Windows znacznie wydłużyły ten proces.

Zjawisko to jest powszechne w inżynierii oprogramowania. Zawsze należy zakładać odpowiedni margines błędu na nieprzewidziane problemy z infrastrukturą, narzędziami, a także weryfikacją samych wymagań biznesowych. Wyliczony stosunek (ratio) czasu rzeczywistego (actual) do początkowo przewidywanego (predicted) wyniósł w tym konkretnym przypadku dokładnie 3.33, co stanowi klasyczny przykład tzw. błędu planowania (planning fallacy) podczas wytwarzania oprogramowania. Wymaga to w przyszłości lepszego szacowania ryzyka i czasu potrzebnego na zapoznanie się ze specyfikacją DORA.