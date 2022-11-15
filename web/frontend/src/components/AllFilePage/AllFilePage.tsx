import axios from "axios"
import { useAppDispatch, useAppSelector } from "../../hook/redux"
import { mainSlice } from "../../store/reducers/MainSlice"
import { Button, Table } from "antd"
import type { ColumnsType } from "antd/es/table"
import React, { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import Navigation from '../Navigetion/Navigation'

interface DataType {
  key: React.Key
  name: string
  path: string
  date: string
  id: string
}

function AllFilePage() {
  const { allFiles } = useAppSelector((state) => state.mainReducer)
  const dispatch = useAppDispatch()
  const { setAllFile, setAllFileSelect } = mainSlice.actions

  const [selectedRowKeys, setSelectedRowKeys] = useState<React.Key[]>([])

  const columns: ColumnsType<DataType> = [
    {
      title: "Name",
      dataIndex: "name",
    },
    {
      title: "Path",
      dataIndex: "path",
    },
    {
      title: "Date",
      dataIndex: "date",
    },
  ]

  const data: DataType[] = []
  for (let i = 0; i < allFiles.length; i++) {
    data.push({
      key: i,
      name: allFiles[i].name,
      path: allFiles[i].path,
      date: allFiles[i].date,
      id: allFiles[i].id,
    })
  }

  const onSelectChange = (newSelectedRowKeys: React.Key[]) => {
    setSelectedRowKeys(newSelectedRowKeys)
    let array = []
    for (let i of newSelectedRowKeys) {
      for (let j of data) {
        if (i === j.key) {
          array.push(j.id)
        }
      }
    }
    console.log(array)
    dispatch(setAllFileSelect(array))
  }

  const rowSelection = {
    selectedRowKeys,
    onChange: onSelectChange,
  }

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/get_all_gpzu").then((data) => {
      dispatch(setAllFile(data.data))
    })
  }, [])

  return (
    <div>
      <div className="w-full h-[56px] flex justify-start items-center border-b-[1px] border-black">
        <Navigation />
        <p className="ml-[20px] text-[20px]">Все файлы</p>
      </div>
      <Link to="/result/">
        <Button type="text" onClick={() => {}}>
          Get Result
        </Button>
      </Link>
      <Table rowSelection={rowSelection} columns={columns} dataSource={data} />
    </div>
  )
}

export default AllFilePage
