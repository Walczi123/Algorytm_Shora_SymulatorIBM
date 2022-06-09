# Algorytm_Shora_SymulatorIBM

Program można uruchomić zarówno na zwykłym komputerze, jak i w symulatorze IBM.

Należy pobrać kod źródłowy ( i w przypadku symulatora IBM przenieść go). W głównym folderze znajduje się plik "project.ipynb". Jest to główny i jedyny plik potrzebny dla użytkownika. Zawiera on listę autorów, oraz 4 komórki z kodem. Uruchamianie komórek z kodem pozwala używać programu.

Pierwsza komórka została opisana etykietą " Zainstaluj niezbędne pakiety". Instaluje ona pakiet stworzony na potrzeby tego projektu oraz bibliotekę Cirq. W razie problemów z uruchamianiem następnych komórek z powodu brakujących pakietów należy doinstalować ręcznie niezbędne pakiety ( użyte biblioteki używają wielu standardowych pakietów jak pandas, numpy).

Druga komórka pozwala uruchomić interfejs służący do faktoryzacji liczb za pomocą trzech funkcji:
1. Shor's algorithm using Qiskit - implementacja algorytmu Shora za pomocą biblioteki Qiskit. Wprowadzone mogą zostać 3 wartości
- liczba poddawana faktoryzacji
- liczba losowa używana do funkcji potęgowania modułowego
- timeout ograniczający czas wykonywania funkcji
2. Function using naive algorithm - implementacja funkcji faktoryzacji za pomocą bibilioteki Cirq bez wykorzystania elementów kwantowych. Wprowadzana jest liczba poddawana faktoryzacji.
3. Shor's algorithm using Cirq - implementacja algorytmu Shora za pomocą biblioteki Cirq. Wprowadzana jest liczba poddawana faktoryzacji.

Trzecia komórka pozwala poddać faktoryzacji liczbę podając wniki dla implementacji z wykorzystaniem bibliotek Qiskit, Cirq, funkcji faktoryzacji bez elementów kwantowych. Uwzględnieniona zostaje wartość timeout dla biblioteki Qiskit. Liczba używana do funkcji potęgowania modułowego ma stałą wartość 2. 

Czwarta komórka pozwala przedstawić wyniki przeprowadzonych testów.
