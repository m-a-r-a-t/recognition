import React from "react"
import axios from "axios"
import { useAppDispatch, useAppSelector } from "../../hook/redux"
import { mainSlice } from "../../store/reducers/MainSlice"
import AllFilePage from "../AllFilePage/AllFilePage"
import { Table } from "antd"
import Navigation from "../Navigetion/Navigation"

function ResultPage() {
  const { allFiles, selectAllFileResult } = useAppSelector(
    (state) => state.mainReducer
  )

  let columns = []
  let data = []

  for (let i in allFiles[0].result) {
    columns.push({ title: i, dataIndex: i })
  }

  for (let i of allFiles) {
    for (let j of selectAllFileResult) {
      if (i.id === j) {
        data.push(i.result)
      }
    }
  }

  return (
    <div className="h-[100vh] w-full overflow-y-auto">
      <div className="w-full h-[56px] flex justify-start items-center border-b-[1px] border-black">
        <Navigation />
        <p className="ml-[50px] text-[20px]">Результат</p>
      </div>
      <div>
        <Table columns={columns} dataSource={data} />
      </div>
    </div>
  )
}

export default ResultPage
