import "./Data.container.scss"

import { DataGrid, GridColDef, GridToolbar } from '@mui/x-data-grid';
import { DataService } from '../../services/data-service/DataService';
import { useEffect, useState } from 'react';
import { Device } from '../../models/Device';
import { Autocomplete, TextField } from '@mui/material';
import { DeviceData } from "../../models/DeviceData";


const columns: GridColDef[] = [
  { field: 'id', headerName: 'Id', width: 200 },
  { field: 'parameter', headerName: 'Parameter', width: 200 },
  { field: 'timestamp', headerName: 'Timestamp', width: 250 },
  { field: 'value', headerName: 'Value', width: 200 },
  { field: 'type', headerName: 'Type', width: 200 }
];

interface SelectAutocompleteProps {
  label: string;
  value: string;
}


export default function DataContainer() {
  const [data, setData] = useState<Device[] | undefined>([]);
  // const [currentDevice, setCurrentDevice] = useState<DeviceInfo | undefined>(undefined);
  const [selectElementPropsData, setSelectElementPropsData] = useState<SelectAutocompleteProps[]>([]);
  const [tableRows, setTableRows] = useState<DeviceData[]>([])



  const generateSelectElementProps = (devices: Device[]): void => {
    const selectConfigs: SelectAutocompleteProps[] = [];
    devices.map(device => {
      if (device.device?.name && device.device?.id) {
        selectConfigs.push({ label: device.device.name, value: device.device.id })
      }
    })
    setSelectElementPropsData(selectConfigs)
  }

  const onSelectItemChanged = (val: SelectAutocompleteProps): void => {
    if (!data?.length) return;
    setTableRows(data?.filter(device => device.device?.name == val.label)[0].device_data || []);
  }

  const generateFullDataRender = (devices: Device[]): void => {
    const tableRows: DeviceData[] = []
    devices?.map(device => {
      tableRows.push(...(device.device_data || []))
    })
    setTableRows(tableRows)
  }

  useEffect(() => {
    async function getData() {
      const response = await DataService.getDeviceData()
      if (!response?.data.length) return
      setData(response.data);
      generateSelectElementProps(response.data)
      generateFullDataRender(response.data)
    }
    getData();
  }, []);


  return (
    <div className='data-container container'>
      <div className='data-container-select'>
        <Autocomplete
          disablePortal
          className="select-auto-complete"
          options={selectElementPropsData}
          sx={{ width: 300 }}
          renderInput={(params) => <TextField {...params} label="Device" />}
          onChange={(event, value) => {
            if (value) onSelectItemChanged(value)
          }}
        />
      </div>

      <div className='data-container data'>
        <div className='data-container-table container' style={{ height: '90vh', width: '100%' }}>
          <DataGrid
            rows={tableRows}
            columns={columns}
            slots={{ toolbar: GridToolbar }}
          />
        </div>
      </div>
    </div>
  );
}