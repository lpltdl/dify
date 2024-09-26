import cn from '@/utils/classnames'

type FileImageRenderProps = {
  imageUrl: string
  className?: string
  alt?: string
  onLoad?: () => void
  onError?: () => void
  showDownloadAction?: boolean
}
const FileImageRender = ({
  imageUrl,
  className,
  alt,
  onLoad,
  onError,
  showDownloadAction,
}: FileImageRenderProps) => {
  return (
    <div className={cn('border-[2px] border-effects-image-frame shadow-xs', className)}>
      <img
        className={cn('w-full h-full object-cover', showDownloadAction && 'cursor-pointer')}
        alt={alt}
        onLoad={onLoad}
        onError={onError}
        src={imageUrl}
        onClick={() => showDownloadAction && window.open(imageUrl, '_blank')}
      />
    </div>
  )
}

export default FileImageRender
