import * as React from "react"
import { List } from "antd"
import { useAppSelector } from "../../../hook/redux"
import { mainSlice } from "../../../store/reducers/MainSlice"

function UploadFileList() {
  const { allFiles, selectAllFileResult } = useAppSelector(
    (state) => state.mainReducer
  )

  const list: any[] = []

  for (let i of allFiles) {
    for (let j of selectAllFileResult) {
      if (i.id === j) {
        list.push({ name: i.name, path: i.path, date: i.date })
      }
    }
  }

  console.log(list)

  return (
    <div>
      {list.map((el) => (
        <div className="mt-[10px] h-auto w-full text-[20px] border-[1px] border-black">
          <p>Name: {el.name}</p>
          <p>Path: {el.path}</p>
          <p>Date: {el.date}</p>
        </div>
      ))}
    </div>
  )
}

export default UploadFileList
