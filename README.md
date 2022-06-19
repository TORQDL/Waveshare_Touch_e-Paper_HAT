# Waveshare Touch e-Paper HAT

## About

Python code for the Waveshare Touch e-Paper HAT series.

Supported Models:
| Model | Product Page | Product Wiki |
| --- | --- | --- |
| 2.13" | [Product Page](https://www.waveshare.com/2.13inch-Touch-e-Paper-HAT.htm) | [Product Wiki](https://www.waveshare.com/wiki/2.13inch_Touch_e-Paper_HAT) |
| 2.9" | [Product Page](https://www.waveshare.com/2.9inch-Touch-e-Paper-HAT.htm) | [Product Wiki](https://www.waveshare.com/wiki/2.9inch_Touch_e-Paper_HAT) |

> For more information, please search on the official website:
> - https://www.waveshare.com
> - https://www.waveshare.com/wiki/Main_Page

## Setup

### Requirements

Supported Raspberry Pi Devices:
- All Raspberry Pi devices that have a standard 40-pin GPIO header.
- All Raspberry Pi Compute Modules that have a standard 40-pin GPIO header on a carrier board.
> 1A+&nbsp;| 1B+&nbsp;| 2B&nbsp;| 2B&nbsp;v1.2&nbsp;| 3A+&nbsp;| 3B&nbsp;| 3B+&nbsp;| 4B&nbsp;| 400&nbsp;| Zero&nbsp;| Zero&nbsp;W/WH&nbsp;| Zero&nbsp;2&nbsp;W&nbsp;| CM&nbsp;| CM2&nbsp;| CM3&nbsp;| CM3+&nbsp;| CM4

Supported Operating Systems:
- Raspberry Pi OS Buster (32-bit or 64-bit)
- Raspberry Pi OS Bullseye (32-bit or 64-bit)
- Ubuntu 22.04 (32-bit or 64-bit)
- Ubuntu 22.04 (32-bit or 64-bit)

Supported Python: 
- Python v2: 2.7
- Python v3: 3.7+

### Python v2

``` bash
$ sudo apt update
$ sudo apt install python-pip
$ sudo apt install python-pil
$ sudo apt install python-numpy
$ sudo apt install python-smbios
$ sudo pip3 install RPi.GPIO
$ sudo pip3 install spidev
```

### Python v3

``` bash
$ sudo apt update
$ sudo apt install python3-pip
$ sudo apt install python3-pil
$ sudo apt install python3-numpy
$ sudo apt install python3-smbios
$ sudo pip3 install RPi.GPIO
$ sudo pip3 install spidev
```

## Usage

> ⚠️ Please note which e-ink screen you are using. If you are using the 2.9" model, then you should use the `TP2in9` scripts, and if you are using the 2.13" model, use the `TP2in13` scripts.

TODO: fill in usage information that documents/explains how to utilize these libraries for writing your own applications withoutput to the Waveshare Touch e-Paper HAT series devices.

## Pin Connections

Pin connections can be found in `\lib\epdconfig.py`
> ```
> EPD    =>    Jetson Nano/RPI(BCM)
> VCC    ->    3.3
> GND    ->    GND
> DIN    ->    10(SPI0_MOSI)
> CLK    ->    11(SPI0_SCK)
> CS     ->    8(SPI0_CS0)
> DC     ->    25
> ERST   ->    17
> BUSY   ->    24
> INT    ->    27
> TRST   ->    22
> SDA    ->    SDA1
> SCL    ->    SCL1
> ```

## Thanks

- [e_paper_weather_display](https://github.com/AbnormalDistributions/e_paper_weather_display) by AbnormalDistributions
- [Touch_e-Paper_HAT](https://github.com/waveshare/Touch_e-Paper_HAT) by Waveshare
