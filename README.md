# 🧠 Deep Learning & Speech Processing Environment Setup

This repository explains how to install **Anaconda**, **Spyder**, **PyTorch**, and other libraries needed for deep learning and speech processing tasks.

## 🚀 Step 1: Install Anaconda
1. Go to [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Download and install **Anaconda** for your operating system (Windows, macOS, or Linux).
3. Verify installation:
   ```bash
   conda --version
   ```

## 🧰 Step 2: Create and activate a new environment
We will create a dedicated environment for Deep Learning and Speech Processing.
```bash
conda create -n dl_env python=3.10
conda activate dl_env
```

## 🧪 Step 3: Install the required libraries
🔹 Option 1 — CPU version (recommended if you do not have a GPU)
```bash
conda install pytorch torchvision torchaudio cpuonly -c pytorch
conda install spyder numpy scipy matplotlib pandas scikit-learn librosa jupyter
pip install soundfile tqdm

🔹 Option 2 — GPU version (for NVIDIA GPUs only)
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda install spyder numpy scipy matplotlib pandas scikit-learn librosa jupyter
pip install soundfile tqdm

## 🧩 Step 4: Launch Spyder
After installation, launch Spyder (in terminal) with:
```bash
spyder
Then go to:
1. Tools → Preferences → Python Interpreter → Use the following interpreter
2. Select the Python executable inside your dl_env environment (this ensures that Spyder uses the same libraries you just installed).

## ✅ Step 5: Verify the installation
Follow the instructions depending on your operating system.

🪟 Windows
1. Open Anaconda Prompt (not CMD).
2. Activate the environment:
```bash
  conda activate dl_env
3. Verify versions:
```bash
  python --version
  conda list pytorch
4. Run the file test_torch_gpu.py from Examples folder:
```bash
  python test_torch_gpu.py
5. To check from Spyder:
```bash
  Open Spyder.
  Load the same test_torch_gpu.py.
  Run it (F5) and check the console output.

🍎 macOS
1. Open Terminal.
2. Activate the environment:
```bash
  conda activate dl_env
3. Verify installation:
```bash
  python --version
  conda list pytorch
4. Run the file test_torch_gpu.py.
```bash
  python test_torch_gpu.py
  💡 Most Macs will show “Running on CPU” because NVIDIA GPUs are not supported.
5. To test from Spyder:
```bash
spyder
Open the file.
Run it (F5).

🐧 Linux (Ubuntu / Debian / Fedora)
1. Open a terminal.
2. Activate your environment:
```bash
  conda activate dl_env
3. Check versions:
```bash
  python --version
  conda list pytorch
4. Run file test_torch_gpu.py from Examples folder:
```bash
  python test_torch_gpu.py
5. If everything works, start Spyder:
```bash
  spyder &
  and run the same file there.

## 🎧 Step 6: Verify audio processing libraries
Run audio_processing_example.py from Examples folder.
```bash
   python audio_processing_example.py
   
If everything is installed correctly, a plot with a waveform will appear.

## 🧠 Summary
You now have a complete environment with all tools needed for Deep Learning and Speech Processing experiments:
   1. Python 3.10
   2. PyTorch, TorchAudio, TorchVision
   3. Spyder IDE
   4. NumPy, SciPy, Matplotlib, Pandas, scikit-learn
   4. Librosa, SoundFile, TQDM, and Jupyter

## 💬 Common issues
1. Spyder not detecting environment: Go to Tools → Preferences → Python Interpreter → Use the following interpreter and select your dl_env path.
2. Librosa error with soundfile: Run pip install soundfile.
3. CUDA not detected: Ensure you installed the correct CUDA toolkit version for your GPU and drivers.

