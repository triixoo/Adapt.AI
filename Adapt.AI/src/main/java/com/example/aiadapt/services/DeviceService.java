package com.example.aiadapt.services;

import com.example.aiadapt.models.Device;
import com.example.aiadapt.repositories.DeviceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DeviceService {

    @Autowired
    private DeviceRepository deviceRepository;

    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }

    public Optional<Device> getDeviceById(Long id) {
        return deviceRepository.findById(id);
    }

    public Device saveDevice(Device device) {
        return deviceRepository.save(device);
    }

    public void deleteDevice(Long id) {
        deviceRepository.deleteById(id);
    }

    public Device toggleDeviceStatus(Long id) {
        Optional<Device> deviceOpt = deviceRepository.findById(id);
        if (deviceOpt.isPresent()) {
            Device device = deviceOpt.get();
            device.setStatus(!device.isStatus()); // Toggle the status
            return deviceRepository.save(device);
        }
        return null;
    }
}
