
# Proyect setup
**Obligatory**: You can install Textual via PyPI, with the following command:

```bash 
pip install textual
```
**Obligatory if you want syntax highlight:**
```bash 
pip install "textual[syntax]"
```

**Optional**: If you plan on developing Textual apps, you should also install textual developer tools:

```bash 
pip install textual-dev
```

## Windows Issues

The Windows long path when attempting to access or create files or folders with paths exceeding the 260-character limit imposed by Windows. 

To enable this feature on Windows, you need to modify the registry:

1. Open the Registry Editor (`regedit`).
2. Navigate to the following path:
   **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem**
3. Locate the corresponding entry (e.g., "LongPathsEnabled" or another relevant key).
4. Set its value from 0 to 1 (hexadecimal) to enable the feature.

**Warning:** Editing the Windows Registry can affect system stability. Proceed with caution and consider backing up the registry before making any changes.
