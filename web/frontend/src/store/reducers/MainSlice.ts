import { createSlice, PayloadAction } from "@reduxjs/toolkit"
// import { fetchData } from './ActionCreater';
import type { UploadFile } from "antd/es/upload/interface"

interface MainState {
  allFiles: Idata[]
  selectAllFileResult: string[]
}

interface Idata {
  id: string
  path: string
  name: string
  date: string
  result: {
      [index: string]: string
  }
}

const initialState: MainState = {
  allFiles: [],
  selectAllFileResult: []
}

export const mainSlice = createSlice({
  name: "main",
  initialState,
  reducers: {
    setAllFile(state, action: PayloadAction<Idata[]>){
      state.allFiles = []
      state.allFiles = action.payload
    },
    setAllFileSelect(state, action: PayloadAction<string[]>){
      state.selectAllFileResult = []
      state.selectAllFileResult = action.payload
    }
  },
  extraReducers: {},
})

export default mainSlice.reducer
