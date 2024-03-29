import { DeviceData } from "./DeviceData";
import { DeviceInfo } from "./DeviceInfo";

export interface Device {
    device?: DeviceInfo;
    device_data?: DeviceData[];
}