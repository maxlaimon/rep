GIL — это своеобразная блокировка, позволяющая только одному потоку управлять интерпретатором питона. Это означает, что в любой момент времени будет выполняться только один какой-нибудь поток. В multiprocessing каждый процесс выполняется независимо от других, этот метод параллелизма позволяет избежать проблем с GIL.