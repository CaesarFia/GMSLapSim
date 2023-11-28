import matlab.engine
eng = matlab.engine.start_matlab()

eng = matlab.engine.start_matlab("-desktop")

eng.quit()

