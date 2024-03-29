import { DeviceDataResponse } from "../../models/DeviceDataResponse";
import axios from "axios";

export class DataService {
    public static async getDeviceData(): Promise<DeviceDataResponse | undefined> {
        let response: DeviceDataResponse | undefined;
        try {
            response = 
                await axios.get(`
                    ${process.env.API_PROTO}://${process.env.API_HOST}:${process.env.API_PORT}/${process.env.API_URL_BASE}/devices`);
        } catch (error) {
            console.log('Error: ', error)
        }

        return response
    }
}